var tableStorageInfo;
init();
show();
function show() {
	tableStorageInfo.show({});
	setTimeout('show();', 2000);
}
function init() {
	var options = {
		title : 'Table Storage Info',
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
			field : 'storefiles',
			title : 'StoreFiles',
			width : 100,
			align : 'center'
		}, {
			field : 'stores',
			title : 'Stores',
			width : 100,
			align : 'center'
		}, {
			field : 'rootIndexSizeKB',
			title : 'rootIndexSizeKB',
			width : 100,
			align : 'center'
		}, {
			field : 'storefileIndexSizeMB',
			title : 'storefileIndexSizeMB',
			width : 100,
			align : 'center'
		}, {
			field : 'storefileSizeMB',
			title : 'storefileSizeMB',
			width : 100,
			align : 'center'
		}, {
			field : 'totalStaticBloomSizeKB',
			title : 'totalStaticBloomSizeKB',
			width : 100,
			align : 'center'
		},{
			field : 'totalStaticIndexSizeKB',
			title : 'totalStaticIndexSizeKB',
			width : 100,
			align : 'center'
		}, {
			field : 'currentCompactedKVs',
			title : 'currentCompactedKVs',
			width : 100,
			align : 'center'
		}, {
			field : 'totalCompactingKVs',
			title : 'totalCompactingKVs',
			width : 100,
			align : 'center'
		}, {
			field : 'memStoreSizeMB',
			title : 'memStoreSizeMB',
			width : 100,
			align : 'center'
		} ] ],
		url : 'http://127.0.0.1:8000/get_table_storage_info/',
		tableId : 'table-storage'
	};
	tableStorageInfo = new Pagination(options);
}