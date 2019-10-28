function getBlogPostData(url) {
  $.ajax({
    url: url,
    type: "get",
    dataType: "json"
  }).done(function(res) {
    // result is None
    let data = res["results"];
    if ($.isEmptyObject(data)) {
      $(".read-more .fa-spinner").hide();
      return;
    }

    //add results in search list
    $.each(data, function(key, value) {
      let html = `<li class="article-list-item"><div class="article-detail"><span class="article-date">${
        value["createdAt"]
      }</span><span class="article-category">${
        value["category"]["name"]
      }</span></div><div class="article-list-container"><h2><a href="/c_${
        value["category"]["id"]
      }/p_${value["id"]}/" target="_blank">${
        value["title"]
      }</a></h2><div class="article-list-containersub"><div class="image-square"><img src="${
        value["imageSquare"]["image"]
      }" alt="${
        value["imageSquare"]["name"]
      }"></div><p class="article-description">${
        value["seoDescription"]
      }...</p></div>`;

      if (0 < value["blogTag"].length) {
        html += `<ul class="article-list-tag">`;
        $.each(value["blogTag"], function(k, v) {
          html += `<li class="tag-list">${v["name"]}</li>`;
        });
        html += `</ul>`;
      }

      html += `</div></li>`;
      $(".article-list").append(html);
    });

    $(".read-more .fa-spinner").hide();
    //nexr is None
    if (res["next"]) {
      $(".read-more-button").show();
      getPageAjaxUrl = res["next"];
    }
  });
}

$(function() {
  $(".read-more-button").on("click", function() {
    $(this).hide();
    $(".read-more .fa-spinner").css("display", "inline-block");
    url = getPageAjaxUrl;
    getBlogPostData(url);
  });
});
