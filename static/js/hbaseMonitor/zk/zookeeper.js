var zk_statistics_info;
init();
show();
function show() {
	zk_statistics_info.show({});
	setTimeout('show();', 2000);
}
function init() {
	var options = {
		title : 'Zookeeper Statistics Info',
		striped : true,
		nowrap : true,
		singleSelect : true,
		pagination : false,
		rownumbers : false,
		fitColumns : true,
		columns : [ [ {
			field : 'zkIp',
			title : 'ZK_IP',
			width : 250,
			align : 'center'
		},{
			field : 'version',
			title : 'zkVersion',
			width : 100,
			align : 'center'
		}, {
			field : 'recieved',
			title : 'Recieved',
			width : 100,
			align : 'center'
		}, {
			field : 'send',
			title : 'Send',
			width : 100,
			align : 'center'
		}, {
			field : 'min_Latency',
			title : 'Min_Latency',
			width : 100,
			align : 'center'
		}, {
			field : 'avg_Latency',
			title : 'Avg_latency',
			width : 100,
			align : 'center'
		}, {
			field : 'max_Latency',
			title : 'Max_Latency',
			width : 100,
			align : 'center'
		}, {
			field : 'connections',
			title : 'Connection_Num',
			width : 100,
			align : 'center'
		},{
			field : 'zxID',
			title : 'ZX_ID',
			width : 100,
			align : 'center'
		}, {
			field : 'mode',
			title : 'Mode',
			width : 100,
			align : 'center'
		}, {
			field : 'nodeCount',
			title : 'Node_Count',
			width : 100,
			align : 'center'
		} ] ],
		url : 'http://127.0.0.1:8000/get_zk_info/',
		tableId : 'zk_statistics_table'
	};
	zk_statistics_info = new Pagination(options);
}

$('#zk_attr_table').propertygrid({   
	url: 'http://127.0.0.1:8000/get_zk_attr/#', 
	showGroup: true,
	scrollbarSize: 0 
}); 