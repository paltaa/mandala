$(document).ready(function() {
    
    $(document).scroll(function (e) {
        var bodyScrollTop = $(window).scrollTop();
        if (bodyScrollTop >= 200) {
            $('header').addClass('active');
        }else {
            $('header').removeClass('active');
        }
    });
    $('#home h2').addClass('show');
    
    //SCROLLTO
    $('.scrollTo').click(function(s) {
        s.preventDefault();
        
        scrollTo($(this));
    });
    
    //MOBILE
    $('.btnMobile').click(function (s) {
        s.preventDefault();
        
        if($(this).hasClass('active')){
            
            $('.btnMobile').removeClass('active');
            $('.menuMobile').removeClass('active');
            $('body').css("overflow", "auto");
        }else{
            
            $('.btnMobile').addClass('active');
            $('.menuMobile').addClass('active');
            $('body').css("overflow", "hidden");
        }
    });
    
    
});


	
//instagram custom function
function instagram(selector,hashtag,totalShow,exclude) {

	var listImgs = '<ul>',
		count = 1,
		total = totalShow, //total images to show
		feed = new Instafeed({
			get: 'tagged',
			tagName: hashtag,
			accessToken: '339525162.54da896.7ae68daf82d948d38ad2b2509841f3ec',
			sortBy: 'most-recent',
			limit: 20,
			resolution: 'thumbnail',
			filter: function(image) {
				var userid = image.user.id,
					username = image.user.username,
					imageURL = image.images.thumbnail.url,
					imageLink = image.link,
					newImg = '<li><a href="'+imageLink+'" title="'+username+'" target="_blank"><img src="'+imageURL+'"></a></li>';

				//exclude user account images
				if(exclude!='') {
					if(userid!=exclude) {
						if(count <= total) {
							listImgs = listImgs + newImg;
						}

						count++;
					}
				} else {
					if(count <= total) {
						listImgs = listImgs + newImg;
					}

					count++;
				}
			},
			after: function() {
				listImgs = listImgs + '</ul>';

				//imprimir html con imagenes
				$(selector).html(listImgs);
			}
		});

	feed.run();

}

//FUNCIONES
function scrollTo(element) {
    var href = element.attr('href');
    var target = $(href).offset().top;
    var speed = 900;
    $("html, body").animate({ scrollTop: target - 120 }, speed);
}