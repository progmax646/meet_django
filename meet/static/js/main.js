// js for async web

// edit status

function edit_status(id){
    date = $('#meet_edit_date'+id).val();
    $.post("/meet/edit", { id: id, date: date})
    .done(function(data) {
      $('#modalEditMeet'+id).modal('hide');
      $('#meet_date'+id).text(date);
    });
}

function delete_meet(id){
    $.post("/meet/delete", { id: id})
    .done(function(data) {
      $('#tr_meet'+id).hide();
      $('#ol_mobile'+id).hide();
    });
}

