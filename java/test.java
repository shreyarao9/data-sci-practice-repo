import java.util.Scanner;
public class test{
   public static void main(){
      Scanner in=new Scanner(System.in);
      System.out.println("Enter a char:");
      String str="";
      str=str+in.next().charAt(0);
      System.out.println(str);
      in.close();
   }
}