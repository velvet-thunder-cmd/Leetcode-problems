class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> h_map=new HashMap <> ();
        for(int i=0;i<nums.length;i++){
            int complement= target-nums[i];
            if (h_map.containsKey(complement)){
                return new int[] {h_map.get(complement),i};
            }
            h_map.put(nums[i],i);
        }
        throw new IllegalArgumentException("no match found");
    }
}
