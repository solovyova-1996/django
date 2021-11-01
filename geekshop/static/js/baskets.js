window.addEventListener("load", () => {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        console.log(t_href.name);
        console.log(t_href.value);

        $.ajax({
            url: '/basket/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result)
            },
        });
        event.preventDefault()
    });

    // $('.products_list').on('click', 'button[type="button"]', function () {
    //     let t_href = event.target;
    //     console.log(t_href.name)
    //     let page_obj = t_href.value;
    //     $.ajax({
    //         type: 'GET',
    //         url: '/basket/add/' + t_href.name + '/',
    //         data: {'page_obj': page_obj},
    //         success: function (data) {
    //             if (data) {
    //                 $('.products_list').html(data.result)
    //             }
    //         },
    //     });
    //     event.preventDefault();
    // });
}, false);