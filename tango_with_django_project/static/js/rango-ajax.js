$(document).ready(function(){

    $('#likes').click(function(){
        var catid = $(this).attr('data-catid');
        $.get('/rango/like_category/', {category_id: catid}, function(data){
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });
    
    // hook up a keyup event handler to the element with id="suggestion"
    $('#suggestion').keyup(function(){
        // the content of the input box is obtained and placed into the query variable
        var query = $(this).val();
        // issue a GET request to /rango/suggest_category/ with 'query' as parameter
        $.get('/rango/suggest_category/', {suggestion: query}, function(data){
                // the HTML element with id=”cats” i.e. the div, is updated with the category list html.
                $('#cats').html(data);
        });
    });
    

    $('.rango-add').click(function(){
        var catid = $(this).attr("data-catid");
        var url = $(this).attr("data-url");
        var title = $(this).attr("data-title");
 
        var me = $(this)
        $.get('/rango/auto_add_page/', {category_id: catid, url: url, title: title}, function(data){
            $('#pages').html(data);
            me.hide();
        });
    });
    
    /* $('.rango-add').click(function(){
        var catid = $(this).attr("data-catid");
        var url = $(this).attr("data-url");
        var title = $(this).attr("data-title");
        var me = $(this)
        $.get('/rango/auto_add_page/', {category_id: catid, url: url, title: title}, function(data){
            $('#pages').html(data);
            me.hide();
        });
    }); */
});

