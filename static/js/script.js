function getBlogPostData(url) {
  $.ajax({
    url: url,
    type: "get",
    dataType: "json"
  }).done(function(res) {
    //nexr is None
    if (res["next"]) {
      $(".read-more-button").show();
      $(".read-more .fas").hide();
    }

    // result is None
    let data = res["results"];
    if ($.isEmptyObject(data)) {
      $(".read-more .fas").hide();
      return;
    }

    //add results in search list
    $.each(data, function(key, value) {
      let html = `<li class="article-list-item"><div class="article-detail"><span class="article-date">${
        value["createdAt"]
      }</span><span class="article-category">${
        value["category"]
      }</span></div><div class="article-list-container"><h2><a href="/c_${
        value["category"]
      }/p_${value["id"]}/">${
        value["title"]
      }</a></h2><div class="article-list-containersub"><div class="image-square"><img src="${
        value["imageSquare"]["image"]
      }" alt="${
        value["imageSquare"]["name"]
      }"></div><p class="article-thumbnail">${
        value["seoDescription"]
      }...</p></div><ul class="article-list-tag">${
        value["blogTag"]
      }</ul></div></li>`;
      $(".article-list").append(html);
    });
  });
}

$(function() {
  $(".read-more-button").on("click", function() {
    $(this).hide();
    $(".read-more .fas").css("display", "inline-block");
    setTimeout(function() {
      getBlogPostData(
        "http://127.0.0.1:8000/api/1.0/blogposts/?limit=10&offset=10"
      );
    }, 5000);
  });
});
