public class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> tmp = ArrayList<>();
        tmp.add(0);
        helper(res, graph, 0, tmp);
        return res;
    } 

    private void helper(List<List<Integer>> res, int[][] graph, int cur, List<Integer> tmp) {
        if (cur == graph.length - 1) {
            res.add(new ArrayList(tmp));
            return;
        }

        for (int next: graph[cur]) {
            tmp.add(next);
            helper(res, graph, next, tmp);
            tmp.remove(tmp.size() - 1);
        }
    }
}
