using IEEE802_15_4

sink       = PacketSink( BPSK, 5, diff_enc = true, verbosity = 0 )
chipfile   = joinpath( dirname(@__FILE__), "ieee802_15_4_900_MHz_sample_chips.dat" )
chipvector = open( readbytes, chipfile )


@time exec( sink, chipvector )
