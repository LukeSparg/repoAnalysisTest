import java.util.ArrayList;

//A comment
public class Test {
  static void myMethod() {
    System.out.println("/*I just got executed!*/");
  }
  /*Testing
  Testing a block comment
  Yay*/ static void myMethod2 () {
    System.out.println("I just got executed again!");
  }

  public static void main(String[] args) {
    
    /* Dummy Comment */ float y;
    
    myMethod();
  }
}

// Outputs "I just got executed!"
