import java.io.*;
import java.util.*;

class Job {
   int id, profit, deadline;
   Job(int x, int y, int z) {
      this.id = x;
      this.deadline = y;
      this.profit = z;
   }
}

class solution {
   // return an array of size 2 having the 0th element equal to the count
   // and 1st element equal to the maximum profit
   int[] JobScheduling(Job arr[], int n) {
      Arrays.sort(arr, (a, b) -> (b.profit - a.profit));

      int max = 0;
      for (int i = 0; i < n; i++) {
         if (arr[i].deadline > max) {
            max = arr[i].deadline;
         }
      }

      int result[] = new int[max + 1];

      for (int i = 1; i <= max; i++) {
         result[i] = -1;
      }

      int countJobs = 0, jobProfit = 0;

      for (int i = 0; i < n; i++) {

         for (int j = arr[i].deadline; j > 0; j--) {

            // Free slot found 
            if (result[j] == -1) {
               result[j] = i;
               countJobs++;
               jobProfit += arr[i].profit;
               break;
            }
         }
      }

      int ans[] = new int[2];
      ans[0] = countJobs;
      ans[1] = jobProfit;
      return ans;

   }
}
class Main {
   public static void main(String[] args) throws IOException {
      Scanner in=new Scanner(System.in);
      System.out.println("Enter the size of array: ");
      int n=in.nextInt();
      Job[] arr = new Job[n];
      for(int i=0;i<n;i++){
         System.out.println("Enter job id, deadline and profit: ");
         int id=in.nextInt();
         int deadline=in.nextInt();
         int profit=in.nextInt();
         arr[i] = new Job(id,deadline,profit);
      }
      solution ob = new solution();

      int[] res = ob.JobScheduling(arr, n);
      System.out.println(res[0] + " jobs were selected with a total profit of " + res[1]);
      in.close();
   }
}
