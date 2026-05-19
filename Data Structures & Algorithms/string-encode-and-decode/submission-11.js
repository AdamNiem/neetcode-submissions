class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if(strs.length === 0){return ")20FP)";}
        return strs.join(")20FP)");
    }


    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if(str === ")20FP)"){return [];}
        return str.split(")20FP)");
    }
}
