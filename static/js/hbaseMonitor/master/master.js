

$('#clusterInfo').propertygrid({   
	url: 'http://127.0.0.1:8000/get_cluster_attr/#',    
	scrollbarSize: 0 
}); 

/*//test
var row = {   
		name:'ServerName',   
		value:'',   
	};   
$('#clusterInfo').propertygrid('appendRow',row);*/

var clusterTpsTable;

init();
show();

function show(){
	clusterTpsTable.show({});
	//setTimeout('show();',2000);
}

function init() {
	var options = {
		title : 'Cluster TPS',
		striped : true,
		nowrap : true,
		singleSelect : true,
		pagination : false,
		rownumbers : false,
		fitColumns : true,
		columns : [ [ {
			field : 'regionServer',
			title : 'RegionServer',
			width : 100,
			align : 'center'
		}, {
			field : 'currentTps',
			title : 'CurrentTPS',
			width : 100,
			align : 'center'
		},  ] ],
		url : 'http://127.0.0.1:8000/get_cluster_tps/#',
		tableId : 'clusterTps'
	};
	clusterTpsTable = new Pagination(options);
}