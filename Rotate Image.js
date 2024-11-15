/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
    let n = matrix.length - 1;
    let original = {};
    for (let i = 0; i <= n; ++i)
        for (let j = 0; j <= n; ++j)
            original[`${i},${j}`] = matrix[i][j];

    for (let i = 0; i <= n; ++i) {
        for (let j = 0; j <= n; ++j) {
            matrix[j][n - i] = original[`${i},${j}`];
        }
    }

    return matrix;
};
