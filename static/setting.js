function fetch_available_settings() {
    fetch('http://doraemon.iis.sinica.edu.tw/vs_self_eval/api?action=get_setting_list')
        .then(function (response) {
            return response.json();
        })
        .then(function (settings) {
            var select = document.getElementById("setting_selection");
            var option = document.createElement("option");
            option.text = "drop down to select";
            select.add(option);
            for (let i in settings) {
                var setting = settings[i];
                var option = document.createElement("option");
                option.text = setting;
                select.add(option);
            }
        })
        .catch(function (error) {
            window.alert(error);
        });
}

function fetch_now_running_stories() {
    fetch('http://doraemon.iis.sinica.edu.tw/vs_self_eval/api?action=get_now_running')
        .then(function (response) {
            return response.json();
        })
        .then(function (now_running) {
            console.log(now_running);
            var e = document.getElementById("now_running");
            e.innerHTML = now_running.join('<br>');

        })
        .catch(function (error) {
            window.alert(error);
        });
}

function fetch_ranked_result() {
    fetch('http://doraemon.iis.sinica.edu.tw/vs_self_eval/api?action=get_rank')
        .then(function (response) {
            return response.json();
        })
        .then(function (story_file2avg_rank) {
            console.log(story_file2avg_rank);
            e = document.getElementById("leaderboard");
            for (story_file in story_file2avg_rank) {
                avg_rank = story_file2avg_rank[story_file]
                e.innerHTML += story_file + ': ' + avg_rank.toString();
                e.innerHTML += '\n';
            }
        })
        .catch(function (error) {
            window.alert(error);
        });
}

var use_files = [];
window.onload = function () {
    fetch_available_settings();
    fetch_now_running_stories();
    fetch_ranked_result();

}

function select_setting() {
    var e = document.getElementById("setting_selection");
    var setting = e.options[e.selectedIndex].text;
    fetch_story_files(setting);
}

function fetch_story_files(setting) {
    fetch('http://doraemon.iis.sinica.edu.tw/vs_self_eval/api?action=get_story_list&setting=' + setting
    )
        .then(function (response) {
            return response.json();
        })
        .then(function (response) {
            var story_file_list = response;
            var e = document.getElementById("story_selection");
            e.options.length = 0;
            var option = document.createElement("option");
            option.text = "drop down to select";
            e.add(option);
            for (let i in story_file_list) {
                var story_file = story_file_list[i];
                var option = document.createElement("option");
                option.text = story_file;
                e.add(option);
            }

        })
        .catch(function (error) {
            window.alert(error);
        });

}

function add_file() {
    var e = document.getElementById("story_selection");
    var e1 = document.getElementById("added_files");
    var story_file = e.options[e.selectedIndex].text;
    use_files.push(story_file);
    e1.innerHTML += story_file + '<br>'

}
function use_these_files() {
    var e = document.getElementById("setting_selection");
    var setting = e.options[e.selectedIndex].text;
    fetch('http://doraemon.iis.sinica.edu.tw/vs_self_eval/api?action=use_these_files&setting=' + setting + '&story_files=' + use_files.join())
        .then(function (response) {
            return response.json();
        })
        .then(function (now_running) {
            console.log(now_running);
            var e = document.getElementById("now_running");
            e.innerHTML = now_running.join('<br>');

        })
        .catch(function (error) {
            window.alert(error);
        });

}