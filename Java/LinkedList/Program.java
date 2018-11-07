import java.util.*;
public class Program{
  public static void main(String args[]){
    LinkedList list = new LinkedList();
    Scanner in = new Scanner(System.in);
    print("Terminate input with -1 \n");
    String value = in.nextLine();
    while(!(value.equals("-1"))){
      Node n = new Node(Integer.parseInt(value));
      value = in.nextLine();
      list.insertAtEnd(n);
    }
  }
  public static void print(String n){
    System.out.print(n);
  }
  public static void print(int n){
    System.out.print(n);
  }
  public static void print(long n){
    System.out.print(n);
  }

}
