// js for async web

// edit status

function edit_status(id){
    date = $('#meet_edit_date'+id).val();
    text = $('#meet_edit_text'+id).val()
    console.log(date, text)
    $.post("/meet/edit", { id: id, date: date, text: text})
    .done(function(data) {
      $('#modalEditMeet'+id).modal('hide');
    });
}

function delete_meet(id){
    $.post("/meet/delete", { id: id})
    .done(function(data) {
      $('#tr_meet'+id).hide();
      $('#ol_mobile'+id).hide();
    });
}
