window.onload = function () {
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
    $('.products_list').on('click', 'a[class="btn btn-outline-success"]', function () {
            let t_href = event.target;
            console.log(t_href)
            console.log(t_href.name)
            let page_id = t_href.value;
            // let csrf_token = $('meta[name="csrf-token"]').attr('content');
            //
            // $.ajaxSetup({
            //     headers: {'X-CSRFToken': csrf_token}
            // });
            $.ajax({
                type: 'GET',
                url: '/basket/add/' + t_href.name + '/',
                data: {'page_id': page_id},
                success: (data) => {
                    if (data) {
                        $('.products_list').html(data.result)
                    }
                },
            });
            event.preventDefault();
        });
};