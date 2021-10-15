window.onload = function () {
    $('.products_list').on('click', 'button[type="button"]', (e) => {
        $(document).on('click', '.product_add', (e) => {
            let t_href = e.target;
            let csrf_token = $('meta[name="csrf-token"]').attr('content');

            $.ajaxSetup({
                headers: {'X-CSRFToken': csrf_token}
            });


            $.ajax({
                type: 'POST',
                url: '/basket/add/' + t_href.name + '/',
                success: function (data) {
                    $('.products_list').html(data.result)
                },
            });
            e.preventDefault();
        });
    });
};

