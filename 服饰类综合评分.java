package 获取服饰类门店;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;


public class a {

	 public static void readFileByLines(String fileName) {  
	        File file = new File(fileName);  
	        BufferedReader reader = null;  
	        try {   
	            reader = new BufferedReader(new FileReader(file));  
	            String tempString = null;  
	            int line = 1;  
	            double rating;
	            double comment;
	            double smax=0;
	            String name=null;
	            // 一次读入一行，直到读入null为文件结束  
	            while ((tempString = reader.readLine()) != null) {  
	                // 显示行号  
	               
	                String[] arr=tempString.split("'overall_rating'");
	                String arr1=null;
	                if(arr.length==2)
	                { 
	                arr1=arr[1];
	                if(arr1.indexOf("comment_num")!=-1)
	                 {String[] arr2=arr1.split(",");
	                 rating=Double.parseDouble(arr2[0].substring(3, arr2[0].length()-1));
	                 comment=Double.parseDouble(arr2[1].substring(17, arr2[1].length()-1));}
	                else
	                {
	                	String[] arr2=arr1.split(",");
		                 rating=Double.parseDouble(arr2[0].substring(3, arr2[0].length()-1));
		                 comment=0;
	                }
	                }
	                else
	                {
	                	rating=0;comment=0;
	                }
				    
	               if(smax<rating)
	               {
	            	   smax=rating;
	            	   String[] arr4=tempString.split(",");
	            	   name=arr4[0].substring(10,arr4[0].length()-1);
	               }
	                 //System.out.println("line " + line + ": rating +" + rating+" commnent +"+comment);
	                line++;  
	            } 
	            System.out.println("好评最高的服饰店  ："+name);
	            reader.close();  
	        } catch (IOException e) {  
	            e.printStackTrace();  
	        } finally {  
	            if (reader != null) {  
	                try {  
	                    reader.close();  
	                } catch (IOException e1) {  
	                }  
	            }  
	        }  
	    }  
	 
	public static void main(String[] args)
	{
		readFileByLines("D://ggd.txt");
	}
}
