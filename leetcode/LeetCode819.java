package leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

public class LeetCode819 {
    public static String mostCommonWord(String paragraph, String[] banned) {
        List<String> wordList = new ArrayList<String>();
        Set<String> bannedSet = new HashSet<String>();
        Map<String, Integer> wordFrequencyMap = new HashMap<String, Integer>();

        for (int i=0; i<banned.length; i++) {
            String bannedWord = banned[i];
            if (!bannedSet.contains(bannedWord)) {
                bannedSet.add(bannedWord);
            }
        }
        System.out.println("\n bannedSet: " + bannedSet);

        String[] words = paragraph.split(" ");
        System.out.println("\n Arrays.toString(words): " + Arrays.toString(words));

        if (words != null) {
            for (int i=0; i<words.length; i++) {
                String rawWord = words[i];
                String preparedWord = null;

                //!?',;.

                if (rawWord.endsWith("!")
                        || rawWord.endsWith("?")
                        || rawWord.endsWith(",")
                        || rawWord.endsWith(";")
                        || rawWord.endsWith(".")) {
                    preparedWord = rawWord.substring(0, rawWord.length() - 1);
                }

            }
        }

        System.out.println("\n wordFrequencyMap: " + wordFrequencyMap);

        return null;
    }

    public static boolean checkValidBannedWord(String word) {
        boolean flag = false;

        if (word != null && word.length() > 0) {
            for (int i=0; i<word.length(); i++) {
                if (word.charAt(i) == '!') {

                }
            }
        }

        return flag;
    }

    public static void main(String[] args) {
        /**
         * Input:
         * paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
         * banned = ["hit"]
         *
         * Output: "ball"
         */

        String paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.";

        String[] bannedWords = new String[] {"hit"};

        System.out.println("\n paragraph: " + paragraph);
        System.out.println(" paragraph.length(): " + paragraph.length());
        System.out.println("\n bannedWords: " + Arrays.toString(bannedWords));

        String commonWord = mostCommonWord(paragraph, bannedWords);
        System.out.println("\n commonWord: " + commonWord);
    }
}
