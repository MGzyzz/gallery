$(document).ready(function() {
                const csrfToken = $('input[name=csrfmiddlewaretoken]').val();
$('.add-favorite').click(function() {
    if (!$(this).hasClass('remove-favorite')) {
        var photoId = $(this).data('photo-id');
        var button = $(this);

        $.ajax({
            url: `/api/photos/${photoId}/favorite/`,
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function(data) {
                if (data.detail === 'You have already liked this publication') {
                    alert('Вы уже добавили это фото в избранное');
                } else {
                    button.removeClass('btn-success add-favorite').addClass('btn-danger remove-favorite').text('Удалить из избранного');
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log(xhr.responseText);
            }
        });
    }
});

$('.remove-favorite').click(function() {
    if (!$(this).hasClass('add-favorite')) {
        var photoId = $(this).data('photo-id');
        var button = $(this);

        $.ajax({
            url: `/api/photos/${photoId}/un_favorite/`,
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function(data) {
                if (data.detail === 'You have not liked this publication') {
                    alert('Вы еще не добавили это фото в избранное');
                } else {
                    button.removeClass('btn-danger remove-favorite').addClass('btn-success add-favorite').text('Добавить в избранное');
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log(xhr.responseText);
            }
        });
    }
});


    $('.delete-button').click(function() {
        var photoId = $(this).data('photo-id');
        if (confirm('Вы уверены, что хотите удалить это фото?')) {
            $.ajax({
                url: `/api/photos/delete/${photoId}`,
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                success: function(data) {
                    window.location.href = '/';
                },
                error: function(xhr, textStatus, errorThrown) {
                    console.log(xhr.responseText);
                }
            });
        }
    });

    $('#cancelButton').click(function() {
        $('#editModal').modal('hide');
    });

    $('.edit-button').click(function() {
        var photoId = $(this).data('photo-id');
        console.log(photoId)
        $('#editModal').modal('show');

        $('#submitEdit').click(function() {
            var signature = $('#signature').val();
            console.log(csrfToken)
            $.ajax({
                url: `/api/photos/update/${photoId}`,
                method: 'PUT',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                data: {
                    signature: signature
                },
                success: function(data) {
                    $('#editModal').modal('hide');
                    $('h1').text(signature)
                },
                error: function(xhr, textStatus, errorThrown) {
                    console.log(xhr.responseText);
                }
            });
        });
    });
});