let dfsOnHTMLNodesPreOrder = (node = document.body) => {

	let stk = [];
	stk.push(node);

	while(stk.length !== 0){

		let currentNode = stk.pop();

		//check for the condiditon or just console.log
		console.log(currentNode);

		if(currentNode && currentNode.childNodes && currentNode.childNodes.length >0){

			for(let i = currentNode.childNodes.length - 1; i>=0; i--){
				stk.push(currentNode.childNodes[i]);
			}
		}
	}

}