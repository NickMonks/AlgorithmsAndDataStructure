const DIRECTIONS = [
    [-2, -1],
    [-2, 1],
    [-1, 2],
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
    [-1, -2]
  ];
  
  const recurse = (N, K, r, c, dp) => {
    if (r < 0 || c < 0 || r >= N || c >= N) {
      return 0;
    }
  
    if (K === 0) {
      return 1;
    }
  
    if (dp[K][r][c] !== undefined) return dp[K][r][c];
  
    let res = 0;
    for (let dir of DIRECTIONS) {
      res += recurse(N, K - 1, r + dir[0], c + dir[1], dp) / 8;
    }
  
    dp[K][r][c] = res;
  
    return dp[K][r][c];
  };
  
  var knightProbability = function(N, K, r, c) {
      // define a matrix of K x N x N 
    const dp = new Array(K + 1).fill(0).map(() => new Array(N).fill(0).map(() => new Array(N).fill(undefined)));
  
    return recurse(N, K, r, c, dp);
  };
  
  console.log(knightProbability(6, 2, 2, 2))