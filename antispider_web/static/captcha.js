$(function () {
    var tracks = document.getElementById('tracks'),
        sliderblock = document.getElementById('sliderblock'),
        isclick = document.getElementById('click')
    slidertips = document.getElementById('slidertips');
    var sliderblockWidth = $('#sliderblock').width();
    var trackWidth = $('#tracks').width();
    var mousemove = false;
    var deviation = 3;

    sliderblock.addEventListener('mousedown', function (e) {
        mousemove = true;
        //    监听mousedown事件，记录滑块起始位置
        startCoordinateX = e.clientX //滑块起始位置
    })
    var distanceCoordianteX = 0; //滑块起始位置
    tracks.addEventListener('mousemove', function (e) {
        if (mousemove) {
            distanceCoordianteX = e.clientX - startCoordinateX; // 滑块当前位置
            if (distanceCoordianteX > trackWidth - sliderblockWidth) {
                // 限制滑块位移距离，避免滑块向右移出滑轨
                distanceCoordianteX = trackWidth - sliderblockWidth;
            } else if (distanceCoordianteX < 0) {
                //通过限制滑块位移距离，避免滑块向左移出滑轨
                distanceCoordianteX = 0;
            }
            // 根据移动距离显示滑块位置
            sliderblock.style.left = distanceCoordianteX + 'px';
        }
    });
    sliderblock.addEventListener('mouseup', function (e) {
        var enCoordinateX = e.clientX;
        verfySliderRetuls(enCoordinateX);

    });

    function verfySliderRetuls(enCoordinateX) { //验证滑动效果
        mousemove = false;
        // 允许误差
        if (Math.abs(enCoordinateX - startCoordinateX - trackWidth) <
            sliderblockWidth + deviation) {
            response = $.ajax({
                url: 'http://127.0.0.1:8206/capt' + urii(),
                type: "GET", async: false,
            });
            var status = $.parseJSON(response.responseText);
            if (status.status) {
                sliderblock.style.color = '#666';
                sliderblock.style.fontSize = '28px';
                sliderblock.style.backgroundColor = '#fff';
                sliderblock.innerHTML = '✔';
                slidertips.style['visibility'] = 'visible';
                // alert('验证成功！');
                isclick.style['visibility'] = 'visible';
                $('#captcha').val(status.validata)
            } else {
                // 如果验证失败，滑块复位
                distanceCoordianteX = 0;
                sliderblock.style.left = 0;
                // alert('验证失败');
            }
        } else {
            // 如果验证失败，滑块复位
            distanceCoordianteX = 0;
            sliderblock.style.left = 0;
            // alert('验证失败');
        }
    }
})