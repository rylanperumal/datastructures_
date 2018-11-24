var tree;
function setup() {
  noCanvas();
  //creating tree object
  tree = new Tree();
  // adding random values to the tree
  for(var i = 0; i < 10; i++){
    tree.addValue(floor(random(0, 100)));
  }
  // printing out the sorted tree
  tree.traverse();
  console.log(tree);
  // searching for a value in the tree
  var result = tree.search(10);
  if(result != null){
    console.log("found");
  }else{
    console.log("not found");
  }
}
