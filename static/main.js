

function select_story_file(){
   var e = document.getElementById("select_story_file"); 
   var story_file = e.options[e.selectedIndex].text;
   if (story_file == 'drop down to select'){
        return;
   }
   fetch('http://dorami.iis.sinica.edu.tw:12588/api?action=select_story_file&story_file='+story_file)
       .then(function(response){
            return response.json();
       })
        .then(function(response){
            var story_ids = response;
            var e1 = document.getElementById("select_story_id");
            e1.innerHTML = "";
            var option = document.createElement("option");
            option.text = "drop down to select";
            e1.add(option);
            for (let i in story_ids) {
                var story_id = story_ids[i];
                var option = document.createElement("option");
                option.text = story_id;
                e1.add(option);
            }
            e1.disabled = false;
       
        })
        .catch(function(error){
            window.alert(error);
        });
}

function select_story_id(){
   var e = document.getElementById("select_story_file"); 
   var story_file = e.options[e.selectedIndex].text;
    var e1 = document.getElementById("select_story_id");
    var story_id = e1.options[e1.selectedIndex].text;
   if (story_id == 'drop down to select'){
        return;
   }
   fetch('http://dorami.iis.sinica.edu.tw:12588/api?action=select_story_id&story_id='+story_id+'&story_file='+story_file)
        .then(function(response){
            return response.json();
        })
        .then(function(obj){
            console.log(obj);
            flickr_ids = obj['flickr_ids'];
            story = obj['story'];
            document.getElementById('story').innerHTML = story;
            for (let i in flickr_ids){
                flickr_id = flickr_ids[i];
                j = (parseInt(i)+1).toString();
                console.log('img'+j);
                var e2 = document.getElementById('img'+j);
                console.log(e2);
                e2.src = 'http://doraemon.iis.sinica.edu.tw/vist_image/all_images/' + flickr_id + '.jpg';
            }
        })
        .catch(function(error){
            window.alert(error);
        });

}
