/*
 *  本js用于分页使用。提供两个方法，即：initDataGrid，showDataGrid。
 *  initDataGrid函数用于初始化分页列表信息，showDataGrid用户请求数据显示列表信息
 */

var DATAGRID_AJAX_TIMEOUT = 10000; // 请求信息ajax超时时间，时间为毫秒

function Pagination(options) {
	this.queryParams = null;
	this.tableObject = null;
	this.options = null;

	this.isInitSuccess = this.init(options);
}

Pagination.prototype.show = function(params) {
	if (this.options.url == null) {
		this.setJsonDataToTableList(params);
	} else {
		this.queryParams = params;
		this.clearTableList();
		this.loadJsonDataFromAjax(1, this.options.pageSize);
	}
};

Pagination.prototype.clearTableList = function() {

	var data = {
		'total' : 0,
		'rows' : []
	};

	
	// 清理上次查看的页数，将页数置为1
	if (this.options.pagination == true) {
		this.tableObject.datagrid('getPager').pagination('options').pageNumber = 1;
	}

	this.tableObject.datagrid('clearSelections');

	this.tableObject.datagrid('loadData', data);
};

Pagination.prototype.init = function(options) {
	// 初始化参数
	if (this.initOptions(options) == false) {
		return false;
	}

	// 设置列表参数
	this.options = options;

	// 获取列表对应的对象
	this.tableObject = $('#' + this.options.tableId);
	if (this.tableObject == null) {
		$.messager.alert('初始化失败', "没有tableId HTML对象", 'error');
		return false;
	}

	// 初始化列表
	this.initTable();

	return true;
};

Pagination.prototype.initTable = function() {
	var checkboxDisable = this.checkboxDisable;
	var checkboxDisableWhenSelectAll = this.checkboxDisableWhenSelectAll;
	var thisObject = this;

	this.tableObject.datagrid({
		columns : this.options.columns,
		frozenColumns : this.options.frozenColumns,
		fitColumns : this.options.fitColumns,
		striped : this.options.striped,
		nowrap : this.options.nowrap,
		idField : this.options.idField,
		pagination : this.options.pagination,
		rownumbers : this.options.rownumbers,
		singleSelect : this.options.singleSelect,
		checkOnSelect : this.options.checkOnSelect,
		selectOnCheck : this.options.selectOnCheck,
		sortName : this.options.sortName,
		sortOrder : this.options.sortOrder,
		remoteSort : this.options.remoteSort,
		showFooter : this.options.showFooter,
		loadFilter : this.options.loadFilter,
		toolbar : this.options.toolbar,
		title : this.options.title,
		fit : false,
		loadMsg : '数据加载中请稍后……',
		onSelect : function(rowIndex, rowData) {
			checkboxDisable(rowIndex, rowData.unselect, thisObject);
		},
		onCheckAll : function(rows) {
			checkboxDisableWhenSelectAll(rows, thisObject);
		}
	});

	if (this.options.pagination == true) {
		this.initPage();
	}
};

Pagination.prototype.checkboxDisable = function(index, disable, thisObject) {
	if (disable == true) {
		thisObject.tableObject.datagrid('unselectRow', index);
	}
};

Pagination.prototype.checkboxDisableWhenSelectAll = function(rows, thisObject) {
	for ( var index in rows) {
		thisObject.checkboxDisable(index, rows[index].unselect, thisObject);
	}
};

Pagination.prototype.initPage = function() {
	var thisObject = this;
	loadJsonDataFromAjax = this.loadJsonDataFromAjax;
	
	this.tableObject.datagrid('getPager').pagination({
		pageSize : this.options.pageSize,
		pageNumber : 1,
		loading : true,
		showPageList : false,
		showRefresh : true,
		beforePageText : '第',
		afterPageText : '页，共{pages}页',
		displayMsg : '共{total}条记录&nbsp;&nbsp;&nbsp;&nbsp;',
		onSelectPage : function(pageNumber, pageSize) {
			loadJsonDataFromAjax(pageNumber, pageSize,thisObject);
		}
	});
};

Pagination.prototype.loadJsonDataFromAjax = function(pageNumber, pageSize,thisObject) {
	if(thisObject == null){
		thisObject = this;
	}
	
	if (thisObject.options.pagination == true) {
		thisObject.queryParams.pageNo = pageNumber;
		thisObject.queryParams.pageSize = pageSize;
	}

	var isShowLoading = thisObject.isShowLoading;
	var handleJsonData = thisObject.handleJsonData;

	$.ajax({
		url : thisObject.options.url, // ajax请求的地址
		type : 'GET', // ajax请求方式
		dataType : 'json', // ajax返回数据格式，注意：1.返回的json数据不能用',必须用"
		// 2.json对象最后属性不能有,号
		timeout : DATAGRID_AJAX_TIMEOUT, // ajax请求超时时间，毫秒计算
		data : thisObject.queryParams, // ajax请求的参数
		beforeSend : function() {
			// 请求数据前，设置加载特效
			isShowLoading(thisObject, true);
		},
		error : function(HttpRequest) {
			// 显示错误提示框 alert(HttpRequest.responseText);
			//$.messager.alert('获取信息失败', "获取信息超时", 'error');
			alert(HttpRequest.responseText);
			isShowLoading(thisObject, false); // 取消加载特效
		},
		success : function(jsonData, textStatus) {
			isShowLoading(thisObject, false); // 取消加载特效
			handleJsonData(thisObject, jsonData); // 获取数据成功后，设置列表数据
		}
	});
};

Pagination.prototype.isShowLoading = function(thisObject, isLoading) {
	if (thisObject.options.pagination == true) {
		thisObject.tableObject.datagrid('getPager').pagination({
			loading : isLoading
		});
	}
};

Pagination.prototype.handleJsonData = function(thisObject, jsonData) {
	
	//过滤特殊字符串
	//jsonData = DATAGRID_filterTransferChar(jsonData);
	
	//jsonData = $.parseJSON(jsonData);
	
	if (jsonData.code == null) {
		$.messager.alert('获取信息失败', '返回信息格式错误', 'error');
		return;
	}

	if (jsonData.code == 500) {
		$.messager.alert('获取信息失败', jsonData.msg, 'info');
		return;
	}

	//取rows数据
	if(jsonData.total>=0){
		if(jsonData.rows==''||jsonData.rows.length <= 0){
			$.messager.alert('警告', '没有查询到相关记录', 'info');
		}
		
		if (thisObject.options.pagination == true) {
			if (jsonData.total == 0) { // 获取的数据的total为0时，表示加载的不是第一页，不能覆盖当前total
				jsonData.total = thisObject.tableObject.datagrid('getPager')
						.pagination('options').total;
			}	
		}
		
		thisObject.setJsonDataToTableList(jsonData, thisObject);
	}
	//老接口，取msg中的数据
	else{
		if (thisObject.options.pagination == true) {
			if (jsonData.msg.total == 0) { // 获取的数据的total为0时，表示加载的不是第一页，不能覆盖当前total
				jsonData.msg.total = thisObject.tableObject.datagrid('getPager')
						.pagination('options').total;
			}	
		}
	
	
		thisObject.setJsonDataToTableList(jsonData.msg, thisObject);
	}
	
	//调用回调函数
	if(thisObject.options.callBack != null){
		thisObject.options.callBack(thisObject.options.callBackParams);
	}
};

// 将数据加载到列表中
Pagination.prototype.setJsonDataToTableList = function(jsonData, thisObject) {
	if (thisObject == null) {
		thisObject = this;
	}

	if (jsonData.total == null) {
		var data = {};
		data.total = 0;
		data.rows = jsonData;
		jsonData = data;
	}

	thisObject.tableObject.datagrid('clearSelections');
	thisObject.tableObject.datagrid('loadData', jsonData); // 将数据加载到列表中

	thisObject.setUnselectRowDisable(jsonData, thisObject);
};

Pagination.prototype.setUnselectRowDisable = function(jsonData, thisObject) {
	var checkBoxName = null;
	var columns = thisObject.options.columns;

	for ( var i in columns) {
		for ( var j in columns[i]) {
			if (columns[i][j].checkbox == true) {
				checkBoxName = columns[i][j].field;
				break;
			}
		}
	}
	if (checkBoxName == null) {
		return;
	}

	var checkList = $('input[name="' + checkBoxName + '"]');

	for ( var index in jsonData.rows) {
		if (jsonData.rows[index].unselect == true) {
			checkList[index].disabled = true;
		}
	}
};

Pagination.prototype.initOptions = function(options) {
	if (options == null) {
		$.messager.alert('初始化失败', "没有设置列表初始化参数", 'error');
		return false;
	}

	if (options.tableId == '' || options.tableId == null) {
		$.messager.alert('初始化失败', "没有设置列表的tableId", 'error');
		return false;
	}

	if (options.fitColumns == null) { // 设置为true将自动使列适应表格宽度以防止出现水平滚动
		options.fitColumns = false;
	}

	if (options.striped == null) { // 设置为true将交替显示行背景
		options.striped = false;
	}

	if (options.nowrap == null) { // 设置为true，当数据长度超出列宽时将会自动截取
		options.nowrap = true;
	}

	if (options.pagination == null) { // 设置true将在数据表格底部显示分页工具栏
		options.pagination = false;
	}

	if (options.rownumbers == null) { // 设置为true将显示行数
		options.rownumbers = false;
	}

	if (options.singleSelect == null) { // 设置为true将只允许选择一行
		options.singleSelect = false;
	}

	if (options.checkOnSelect == null) { // 如果为
		// true，当用户点击一行时,进行选择；如果为false，点击checkbox时，进行选择
		options.checkOnSelect = true;
	}

	if (options.selectOnCheck == null) { // 如果设置为true，点击checkbox将永远选择这行。如果设置为false，选择一个行将不会选择checkbox
		options.selectOnCheck = true;
	}

	if (options.remoteSort == null) { // 定义是否通过远程服务器对数据排序
		options.remoteSort = true;
	}

	if (options.showFooter == null) { // 定义是否显示行底（如果是做统计表格，这里可以显示总计等）。
		options.showFooter = true;
	}

	if (options.sortOrder == null) {
		options.sortOrder = 'asc';
	}

	if (options.queryParams == null) {
		options.queryParams = {};
	}

	if (options.pageSize == null) {
		options.pageSize = 15;
	}

	return true;
};


function DATAGRID_filterTransferChar(data) {

	data=data.replace(/\\n/g,"<br/>");
	data=data.replace(/\\r/g,"");
	data=data.replace(/\\t/g,"");
//  对于单纯的\不做转换
//	data=data.replace(/\\/g,"");
	
	return data;
}

