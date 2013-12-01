
var navigation_menu = {'menus':[
	{'menu_id':'main1','menu_title':'HBase Table Info',
		'menu_children':[
			{'menu_id':'main1_minor1','menu_title':'Table TPS','url':'http://127.0.0.1:8000/show_table_tps/#'},
			{'menu_id':'main1_minor2','menu_title':'Table Storage Info','url':'http://127.0.0.1:8000/show_table_storage_info/#'},
		]
	},
	{'menu_id':'main2','menu_title':'HBase Region Info',
		'menu_children':[
			{'menu_id':'main2_minor1','menu_title':'订单管理','url':'order.html'},
			{'menu_id':'main2_minor2','menu_title':'订单管理','url':'order.html'},
			{'menu_id':'main2_minor3','menu_title':'订单管理','url':'order.html'}
		]
	},
	{'menu_id':'main3','menu_title':'HBase Master Info',
		'menu_children':[
			{'menu_id':'main3_minor1','menu_title':'Cluster Info','url':'order.html'},
			{'menu_id':'main3_minor2','menu_title':'Master  Info','url':'order.html'},
			{'menu_id':'main3_minor3','menu_title':'RegionServer Load','url':'order.html'}
		]
	},
	{'menu_id':'main4','menu_title':'HBase RegionServer Info',
		'menu_children':[
			{'menu_id':'main4_minor1','menu_title':'Replication Statistics','url':'order.html'},
			{'menu_id':'main4_minor2','menu_title':'Static Index & Bloom','url':'order.html'},
			{'menu_id':'main4_minor3','menu_title':'Compact & split','url':'order.html'},
			{'menu_id':'main4_minor4','menu_title':'Requests','url':'order.html'},
			{'menu_id':'main4_minor5','menu_title':'Memstore','url':'order.html'},
			{'menu_id':'main4_minor6','menu_title':'Flush','url':'order.html'}
		]
	},
	{'menu_id':'main5','menu_title':'HBase RPC Info',
		'menu_children':[
			{'menu_id':'main4_minor1','menu_title':'订单管理','url':'order.html'},
			{'menu_id':'main4_minor2','menu_title':'订单管理','url':'order.html'},
			{'menu_id':'main4_minor3','menu_title':'订单管理','url':'order.html'}
		]
	},
	{'menu_id':'main6','menu_title':'HBase Month Report',
		'menu_children':[
			{'menu_id':'main4_minor1','menu_title':'订单管理','url':'order.html'},
			{'menu_id':'main4_minor2','menu_title':'订单管理','url':'order.html'},
			{'menu_id':'main4_minor3','menu_title':'订单管理','url':'order.html'}
		]
	},
	{'menu_id':'main7','menu_title':'其他 信息',
		'menu_children':[
			{'menu_id':'main4_minor1','menu_title':'订单管理','url':'order.html'},
			{'menu_id':'main4_minor2','menu_title':'订单管理','url':'order.html'},
			{'menu_id':'main4_minor3','menu_title':'订单管理','url':'order.html'}
		]
	}
]};



$(document).ready(function(){
	var navigation_obj = $('#navigation');
		
	create_navigation(navigation_obj);

	init_navigation();
});

function create_navigation(obj)
{
	var menu_html = '';
	
	obj.empty(); //清空导航菜单的内容
	$.each(navigation_menu.menus, function(i, menu){
		menu_html +='<div id="' + menu.menu_id + '" title="' + menu.menu_title + '" style="overflow:auto;padding:10px;" >';
		
		$.each(menu.menu_children, function(j, menu_children){
			menu_html += '<button type="button" href="#" id="'+menu_children.menu_id+'" class="btn btn-info" rel="' +menu_children.url+'" ';
			menu_html += 'style="width:200px;margin:3px" >' +'<strong>'+menu_children.menu_title+'</strong>'+ '</button><br/>';
		});
		menu_html += '</div>';
	});
	obj.append(menu_html);
	
	$('.btn-info').linkbutton({
		disable:false
	});

	obj.accordion({
		border:true
	});
}

function init_navigation()
{
	var menus = navigation_menu.menus;
	
	if(menus.length>0 && menus[0].menu_children.length > 0)
	{
		add_tabs(menus[0].menu_children[0].menu_title, menus[0].menu_children[0].url);
	}

	$('.btn-info').click(function(){
		var title = $(this).text();
		var url = $(this).attr("rel");
		
		add_tabs(title,url);
	});
}

function add_tabs(title, url)
{
	var content_tabs = $('#content');

	if(!$('#content').tabs('exists',title)){
		content_tabs.tabs('add',{
			title:title,
			//content:createFrame(url),
			href:url,
			closable:true
		});
	}else{
		$('#content').tabs('select',title);
	}
}

function createFrame(url)
{
	//url = 'http://127.0.0.1:8000/test2/#';
	//var s = '<iframe scrolling="auto" frameborder="0"  src="'+url+'" style="width:100%;height:100%;"></iframe>';
	var s = '<iframe frameborder="0"  src="'+url+'" style="width:99%;height:99%;"></iframe>';
	//var s = '<div style="margin:10px;width:700px;height:500px;background-color:#FFA500;">123</div>'
	return s;
}


