public class Node{
  int value;
  Node next;

  // constructor
  Node(int value){
    this.value = value;
  }

  // printer function
  public static void print(Node n){
    System.out.println(n.value);
  }
}
