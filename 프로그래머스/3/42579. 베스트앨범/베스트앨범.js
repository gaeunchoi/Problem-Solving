function solution(genres, plays) {
    let genreMap = new Map();  // { 장르: 총 재생 횟수 }
    let songMap = new Map();   // { 장르: [(고유 번호, 재생 횟수), ...] }

    // 장르별 총 재생 횟수 및 곡 정보 저장
    genres.forEach((genre, index) => {
        let playCount = plays[index];

        // 장르별 총 재생 횟수 저장
        genreMap.set(genre, (genreMap.get(genre) || 0) + playCount);
        
        // 장르별 곡 리스트 저장
        if (!songMap.has(genre)) songMap.set(genre, []);
        songMap.get(genre).push([index, playCount]);
    });

    // 장르별 총 재생 횟수 기준으로 내림차순 정렬
    let sortedGenres = [...genreMap.entries()]
        .sort((a, b) => b[1] - a[1])
        .map(entry => entry[0]); // 장르명만 추출
		
    let bestAlbum = [];

    // 각 장르별로 곡 선택 (최대 2곡)
    for (let genre of sortedGenres) {
        let songs = songMap.get(genre);

        // 재생 횟수 내림차순, 같으면 고유 번호 오름차순 정렬
        songs.sort((a, b) => b[1] - a[1] || a[0] - b[0]);

        // 최대 2곡 선택하여 베스트 앨범에 추가
        bestAlbum.push(...songs.slice(0, 2).map(song => song[0]));
    }

    return bestAlbum;
}