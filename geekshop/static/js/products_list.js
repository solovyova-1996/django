window.onload = function () {
    $('.products_list').on('click', 'a[class="btn-outline-success"]', (e) => {
        $(document).on('click', '.product_list', (e) => {
            let t_href = e.target;
            console.log(t_href)
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
            e.preventDefault();
        });
    });
};

