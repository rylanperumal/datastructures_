import java.util.*;
public class Tester{
  public static final String ANSI_RESET = "\u001B[0m";
  public static final String ANSI_GREEN = "\u001B[32m";
  public static final String ANSI_RED = "\u001B[31m";

  public static final String ANSI_GREEN_BACKGROUND = "\u001B[32m";
  public static final String ANSI_RED_BACKGROUND = "\u001B[31m";


  public static void main(String args[]){
    int score = 0;
    LinkedList list = new LinkedList();
    if(test1(list)){
      print(ANSI_GREEN);
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("         Testcase 1" + "\n");
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("           25/ 25 \n");
      print("++++++++++++++++++++++++++++++++ \n" + ANSI_RESET);
      score = score + 25;

    }else if(!test1(list)){
      print(ANSI_RED);
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("         Testcase 1" + "\n");
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("           0 / 25 \n");
      print("++++++++++++++++++++++++++++++++ \n" + ANSI_RESET);
    }
    if(test2(list)){
      print(ANSI_GREEN);
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("         Testcase 2" + "\n");
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("           25 / 25 \n");
      print("++++++++++++++++++++++++++++++++ \n" + ANSI_RESET);
      score = score + 25;

    }else if(!test2(list)){
      print(ANSI_RED);
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("         Testcase 2" + "\n");
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("           0 / 25 \n");
      print("++++++++++++++++++++++++++++++++ \n" + ANSI_RESET);
    }
    if(test3(list)){
      print(ANSI_GREEN);
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("         Testcase 3" + "\n");
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("           25 / 25 \n");
      print("++++++++++++++++++++++++++++++++ \n" + ANSI_RESET);
      score = score + 25;

    }else if(!test3(list)){
      print(ANSI_RED);
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("         Testcase3" + "\n");
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("           0 / 25 \n");
      print("++++++++++++++++++++++++++++++++ \n" + ANSI_RESET);
    }
    if(test4(list)){
      print(ANSI_GREEN);
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("         Testcase 4" + "\n");
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("           25 / 25 \n");
      print("++++++++++++++++++++++++++++++++ \n" + ANSI_RESET);
      score = score + 25;

    }else if(!test4(list)){
      print(ANSI_RED);
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("         Testcase 4" + "\n");
      print("++++++++++++++++++++++++++++++++" + "\n");
      print("           0 / 25 \n");
      print("++++++++++++++++++++++++++++++++ \n" + ANSI_RESET);
    }
    print(ANSI_GREEN + "Score: ");
    print(score);
    print(" %");
    print(ANSI_RESET);
    print("\n");

  }
  public static boolean test1(LinkedList list){
    // test insertAtEnd, test search
    list.insertAtEnd(new Node(3));
    list.insertAtEnd(new Node(10));
    list.insertAtEnd(new Node(12));
    list.insertAtEnd(new Node(100));
    list.insertAtEnd(new Node(90));
    list.insertAtEnd(new Node(7));
    list.insertAtEnd(new Node(67));
    list.insertAtEnd(new Node(54));
    boolean passed = false;
    if(list.search(54)){
      passed = true;
    }
    return passed;
  }
  public static boolean test2(LinkedList list){
    boolean passed = false;
    if(list.search(54)){
      passed = true;
    }
    return passed;
  }
  public static boolean test3(LinkedList list){
    boolean passed = false;
    list.insertInFront(new Node(70));
    if(list.search(70)){
      passed = true;
    }
    return passed;
  }
  public static boolean test4(LinkedList list){
    boolean passed = false;
    list.delete(90);
    if(!(list.search(90))){
      passed = true;
    }
    return passed;
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
