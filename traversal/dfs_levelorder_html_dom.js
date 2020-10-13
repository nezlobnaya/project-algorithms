let bfsOnHTMLNodes = (node = document.body) => {

    let queue = [];
    queue.push(node);

    while (queue.length !== 0) {

        let currentNode = queue.shift();

        //check for the condiditon or just console.log
        console.log(currentNode);

        if (currentNode && currentNode.childNodes && currentNode.childNodes.length > 0) {

            for (let i = 0; i < currentNode.childNodes.length; i++) {
                queue.push(currentNode.childNodes[i]);
            }
        }
    }

}