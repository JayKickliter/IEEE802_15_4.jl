using IEEE802_15_4
using ZMQ

sink  = PacketSink( BPSK, 5, diff_enc = true, verbosity = 0 )
ctx   = Context( 1 )
zsock = Socket( ctx, PULL )

connect( zsock, "tcp://localhost:5555" )

while true
    msg = recv( zsock )
    out = convert( IOStream, msg )
    bytes = takebuf_array( out )
    exec( sink, bytes )
end