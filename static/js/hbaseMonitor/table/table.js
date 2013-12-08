var tableTpsTable;

init();
show();

function show() {
	tableTpsTable.show({});
	setTimeout('show();', 2000);
}

function init() {
	var options = {
		title : 'Table TPS',
		striped : true,
		nowrap : true,
		singleSelect : true,
		pagination : false,
		rownumbers : false,
		fitColumns : true,
		columns : [ [ {
			field : 'tableName',
			title : 'TableName',
			width : 100,
			align : 'center'
		}, {
			field : 'writeCount',
			title : 'WriteCount',
			width : 100,
			align : 'center'
		}, {
			field : 'readCount',
			title : 'ReadCount',
			width : 100,
			align : 'center'
		}, {
			field : 'totalCount',
			title : 'TotalCount',
			width : 100,
			align : 'center'
		}, {
			field : 'writeTPS',
			title : 'WriteTPS',
			width : 100,
			align : 'center'
		}, {
			field : 'readTPS',
			title : 'ReadTPS',
			width : 100,
			align : 'center'
		} ] ],
		url : 'http://127.0.0.1:8000/get_table_tps/',
		tableId : 'tableTps'
	};
	tableTpsTable = new Pagination(options);
}