/*
ID: your_id_here
LANG: JAVA
TASK: test
*/
import java.io.*;
import java.util.*;

class Main {
  public static void main (String [] args) throws IOException {
    // Use BufferedReader rather than RandomAccessFile; it's much faster
    BufferedReader f = new BufferedReader(new FileReader("greedy.in"));
                                                  // input file name goes above
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("greedy.out")));
    // Use StringTokenizer vs. readLine/split -- lots faster
    StringTokenizer st = new StringTokenizer(f.readLine());
						  // Get line, break into tokens
    int n = Integer.parseInt(st.nextToken());    // first integer
    int count = 0;
    
    st = new StringTokenizer(f.readLine());
    
    for(int i=0; i<n; i++)
      if(Integer.parseInt(st.nextToken()) == 0)
        count += 1;
        
    out.println(count);                           // output result
    out.close();                                  // close the output file
  }
}
