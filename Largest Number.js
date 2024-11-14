/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    let res = nums.map(num => `${num}`).sort((n1, n2) => {
        return `${n2}${n1}` - `${n1}${n2}`;
    }).reduce((p, c) => p += c, '');

    for (let i = 0; i < res.length; ++i) if (res[i] !== '0') return res;
    return '0';
};
