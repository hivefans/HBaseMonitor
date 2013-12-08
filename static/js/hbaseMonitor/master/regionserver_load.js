
var regionInfoTable;
var regionServerInfoTable;

init();
show();

function show() {
	regionInfoTable.show({});
	regionServerInfoTable.show({});
	setTimeout('show();', 2000);
}

function init() {
	var region_info_options = {
		title : 'Region Info',
		striped : true,
		nowrap : true,
		singleSelect : true,
		pagination : false,
		rownumbers : false,
		fitColumns : true,
		columns : [ [ {
			field : 'readRequestCount',
			title : 'ReadRequestCount',
			width : 100,
			align : 'center'
		}, {
			field : 'writeRequestCount',
			title : 'WriteRequestCount',
			width : 100,
			align : 'center'
		}, {
			field : 'readCount',
			title : 'RequestCount',
			width : 100,
			align : 'center'
		}, {
			field : 'stores',
			title : 'Stores',
			width : 100,
			align : 'center'
		}, {
			field : 'storeFiles',
			title : 'StoreFiles',
			width : 100,
			align : 'center'
		}, {
			field : 'memStoreSizeMB',
			title : 'MemStoreSizeMB',
			width : 100,
			align : 'center'
		}, {
			field : 'storeFileSizeMB',
			title : 'StoreFileSizeMB',
			width : 100,
			align : 'center'
		}, {
			field : 'RootIndexSizeKB',
			title : 'rootIndexSizeKB',
			width : 100,
			align : 'center'
		}, {
			field : 'storeFileIndexSizeMB',
			title : 'StoreFileIndexSizeMB',
			width : 100,
			align : 'center'
		}, {
			field : 'totalStaticBloomSizeKB',
			title : 'TotalStaticBloomSizeKB',
			width : 100,
			align : 'center'
		}, {
			field : 'totalStaticIndexSizeKB',
			title : 'TotalStaticIndexSizeKB',
			width : 100,
			align : 'center'
		}, {
			field : 'currentCompactedKVs',
			title : 'CurrentCompactedKVs',
			width : 100,
			align : 'center'
		}, {
			field : 'totalCompactingKVs',
			title : 'TotalCompactingKVs',
			width : 100,
			align : 'center'
		} ] ],
		url : 'http://127.0.0.1:8000/get_region_info/',
		tableId : 'regionInfo'
	};
	var regionServer_info_options = {
		title : 'Region Server Info',
		striped : true,
		nowrap : true,
		singleSelect : true,
		pagination : false,
		rownumbers : false,
		fitColumns : true,
		columns : [ [ {
			field : 'regionServerName',
			title : 'RegionServerName',
			width : 100,
			align : 'center'
		},{
			field : 'load',
			title : 'Load',
			width : 100,
			align : 'center'
		}, {
			field : 'memStoreSizeInMB',
			title : 'MemStoreSizeInMB',
			width : 100,
			align : 'center'
		}, {
			field : 'usedHeapMB',
			title : 'UsedHeapMB',
			width : 100,
			align : 'center'
		}, {
			field : 'maxHeapMB',
			title : 'MaxHeapMB',
			width : 100,
			align : 'center'
		}, {
			field : 'storeFiles',
			title : 'StoreFiles',
			width : 100,
			align : 'center'
		}, {
			field : 'storeFileIndexSizeMB',
			title : 'StoreFileIndexSizeMB',
			width : 100,
			align : 'center'
		}, {
			field : 'storeFileSizeInMB',
			title : 'rootIndexSizeKB',
			width : 100,
			align : 'center'
		}, ] ],
		url : 'http://127.0.0.1:8000/get_regionserver_info/',
		tableId : 'regionserverInfo'
	};
	regionInfoTable = new Pagination(region_info_options);
	regionServerInfoTable = new Pagination(regionServer_info_options);
}

$('#regionList').tree({   
    url:'http://127.0.0.1:8000/get_region_list/',
    loadFilter: function(data){   
        if (data.rows){   
            return data.rows;   
        } else {   
            return data;   
        }   
    }   
}); 