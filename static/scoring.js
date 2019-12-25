
function fetch_now_running_stories() {
    fetch('http://doraemon.iis.sinica.edu.tw/vs_self_eval/api?action=get_now_running')
        .then(function (response) {
            return response.json();
        })
        .then(function (now_running) {
            console.log(now_running);
            var e = document.getElementById("now_running");
            e.innerHTML = now_running.join();

        })
        .catch(function (error) {
            window.alert(error);
        });
}

function load_story_to_score() {
    fetch('http://doraemon.iis.sinica.edu.tw/vs_self_eval/api?action=get_stories_to_rank')
        .then(function (response) {
            return response.json();
        })
        .then(function (obj) {
            const story_id = obj['story_id'];
            const images = obj['images']
            const story_list = obj['story_list']
            var count = 0;
            for (var i in story_list) {
                var team = story_list[i][0];
                var story = story_list[i][1];

                var e = document.getElementById('stories');
                var e1 = document.createElement('div');
                count = count + 1;
                e1.innerHTML = count + '. ' + story;
                e1.id = team;
                e1.style.margin = "1%";
                e.appendChild(e1);
            }

            // put images
            for (let i in images) {
                flickr_id = images[i];
                j = (parseInt(i) + 1).toString();
                var e2 = document.getElementById('img' + j);
                e2.src = 'http://doraemon.iis.sinica.edu.tw/vist_image/all_images/' + flickr_id + '.jpg';
            }
        })
        .catch(function (error) {
            window.alert(error);
        });

}

window.onload = function () {
    fetch_now_running_stories();
    load_story_to_score();

}
function submit_score() {
    e = document.getElementById("ranking");
    var ranking = e.value;
    console.log(ranking);
    ranking_list = [];
    if (ranking.length != document.getElementById("stories").children.length) {
        alert("Your input number is different from the given stories");
        return;
    }
    console.log(ranking);
    for (i in ranking) {
        var index = ranking[i];
        console.log('index', index);
        var index = parseInt(index);
        var story_file = document.getElementById("stories").children[index - 1].getAttribute('id');;
        ranking_list.push(story_file);
    }
    fetch('http://doraemon.iis.sinica.edu.tw/vs_self_eval/api?action=ranking&ranks=' + ranking_list.join())
        .then(function () {
            location.reload();
        })
        .catch(function (error) {
            window.alert(error);
        });

}