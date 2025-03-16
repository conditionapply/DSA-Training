public class TestOne{
    public static void main(String args[]){
        int[] nums ={2,3,4};
        int target =6;
        for(int i =0; i<nums.length; i++){
            for(int j =i+1;j<nums.length;j++){
                if(nums[i] + nums[j]==target){
                    System.out.println("["+i+","+j+"]");
                }
            }
        }

    }
 }