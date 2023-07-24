function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


$(".incbut_q").on('click',function(ev)
{
const request = new Request(
    'http://127.0.0.1:8000/upvote_q/',
    {
        headers:{
            'X-CSRFToken':csrftoken,
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
        },
        method:'POST',
        body: 'id='+$(this).data('id')
    }
);
fetch(request).then(function(response){
    console.log('like');
});
});


$(".decbut_q").on('click',function(ev)
{
const request = new Request(
    'http://127.0.0.1:8000/downvote_q/',
    {
        headers:{
            'X-CSRFToken':csrftoken,
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
        },
        method:'POST',
        body: 'id='+$(this).data('id')
    }
);
fetch(request).then(function(response){
    console.log('dislike');
});
});


$(".incbut_a").on('click',function(ev)
{
const request = new Request(
    'http://127.0.0.1:8000/upvote_a/',
    {
        headers:{
            'X-CSRFToken':csrftoken,
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
        },
        method:'POST',
        body: 'id='+$(this).data('id')
    }
);
fetch(request).then(function(response){
    console.log('like');
});
});


$(".decbut_a").on('click',function(ev)
{
const request = new Request(
    'http://127.0.0.1:8000/downvote_a/',
    {
        headers:{
            'X-CSRFToken':csrftoken,
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
        },
        method:'POST',
        body: 'id='+$(this).data('id')
    }
);
fetch(request).then(function(response){
    console.log('dislike');
});
});


$(".correct").on('click',function(ev)
{
const request = new Request(
    'http://127.0.0.1:8000/correct/',
    {
        headers:{
            'X-CSRFToken':csrftoken,
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
        },
        method:'POST',
        body: 'id='+$(this).data('id')
    }
);


fetch(request).then(
    response_raw =>response_raw.json().then(function(response_json)
    {
    const comment = document.querySelector(`[data-id=${$(this).data('id)}`);
    response_json.isRight === true? comment.setAttribute('checked'):removeAttribute('checked');
    }
    )
);
});
