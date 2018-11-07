public class LinkedList{
  Node head;
  Node tail;

  LinkedList(){
    this.head = new Node(-1);
    this.tail = new Node(-1);
    this.head.next = this.tail;
  }

  public void insertInFront(Node n){
    n.next = this.head.next;
    this.head.next = n;
  }
  public void insertAtEnd(Node n){
    Node curr = this.head;
    while(curr.next != this.tail){
      curr = curr.next;
    }
    curr.next = n;
    n.next = tail;
  }
  public boolean search(int value){
    boolean exists = false;
    Node curr = this.head.next;
    while(curr != this.tail){
      if(curr.value == value){
        exists = true;
      }
      curr = curr.next;
    }
    return exists;
  }
  public void delete(int value){
    Node curr = this.head.next;
    Node prev = this.head;
    while(curr != this.tail){
      if(curr.value == value){
        prev.next = curr.next;
        curr = null;
        return;
      }
      prev = prev.next;
      curr = curr.next;
    }
  }
  public void print(){
    Node curr = this.head.next;
    while(curr != this.tail){
      System.out.println(curr.value);
      curr = curr.next;
    }
  }
}
