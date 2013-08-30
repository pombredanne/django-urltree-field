var UrlTree = {
    // this is set automatically
    admin_media_prefix: '',
    
    init: function() {
        // Deduce admin_media_prefix by looking at the <script>s in the
        // current document and finding the URL of *this* module.
        var scripts = document.getElementsByTagName('script');
        for (var i=0; i<scripts.length; i++) {
            if (scripts[i].src.match(/urltree/)) {
                var idx = scripts[i].src.indexOf('urltree/js/urltree.js');
                UrlTree.admin_media_prefix = scripts[i].src.substring(0, idx);
                break;
            }
        }
    },
    // show urltree
    show: function(id, href, close_func) {
        // var id2=String(id).split(".").join("___");
        var id2=String(id).replace(/\-/g,"____").split(".").join("___");
        UrlTreeWindow = window.open(href, String(id2), 'height=600,width=960,resizable=yes,scrollbars=yes');
        UrlTreeWindow.focus();
        if (close_func) {
            UrlTreeWindow.onbeforeunload = close_func;
        }
    }
}

function addEvent( obj, type, fn ) {
    if ( obj.attachEvent ) {
        obj['e'+type+fn] = fn;
        obj[type+fn] = function(){obj['e'+type+fn]( window.event );}
        obj.attachEvent( 'on'+type, obj[type+fn] );
    } else
        obj.addEventListener( type, fn, false );
}

addEvent(window, 'load', UrlTree.init);
