// Messenger构造函数
function Messenger(desObject, desRegion) {
	this.registerMap = null; // 收到消息的类型以及收到该类型的消息后的动作
	this.iframeObject = null; // 发送消息的目的地iframe 对象
	this.region = null; // 检查域名

	this.init(desObject, desRegion);
}

Messenger.prototype.register = function(code, callBack) {
	this.registerMap[code] = callBack;
};

Messenger.prototype.init = function(desObject, desRegion) {
	registerMap = new Array();
	this.iframeObject = desObject;
	if (desRegion == null) {
		this.region = '*';
	} else {
		this.region = desRegion;
	}

	window.addEventListener('message', this.receiveMsg, false);
};

Messenger.prototype.receiveMsg = function(event) {
	if ((this.region != '*') && (event.origin.indexOf(this.region) < 0)) {
		return;
	}

	var data = event.data;
	if (data.code != null) {
		this.registerMap[data.code](data.value);
	}
};

Messenger.prototype.send = function(code,value) {
	var data = new Object();
	data.code = code;
	data.value = value;

	this.iframeObject.postMessage(data,this.region);
};

