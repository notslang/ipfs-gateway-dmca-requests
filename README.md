# IPFS Gateway DMCA Requests

I currently operate an IPFS gateway on [ipfs.slang.cx](https://ipfs.slang.cx). I don't publish or pin any content there, it's only a resolver for content that's available on the rest of the IPFS network.

I get a lot of DMCA requests from running this. Currently I'm blocking 12367 files. They're almost all books, although I don't have nearly enough time to go through them manually.

This repository holds all of the DMCA requests I've been sent, along with code for generating an [nginx](https://www.nginx.com/) config that I use for blocking requests for those files on my gateway. Whenever I get a request I add it to the repo and then update the nginx config to block whatever they're asking me to block.

If I've blocked a non-copyrighted file, let me know and I'll remove it.

## Where do these DMCA requests come from?

The requests themselves are usually sent to me by a guy named Gareth Young, and sometimes by Emma Hart or Robert Caple. I'm pretty sure that they all work for a big law firm called [Covington and Burling](https://www.cov.com) in London. They seem to have a history of sending [frivolous DMCA claims](http://www.gregthatcher.com/Financial/THATCHER_TO_HOWARD_00910320130823171232.pdf), so I wouldn't be surprised if they're responsible for this.

The tool that they use for sending the requests is called [CIU Online](https://www.ciu-online.net). I don't know what "CIU" stands for, but it's probably not the university. It looks like a home-grown ASP.NET application, but the way it works is a bit of a puzzle to me.

The weird thing is, it doesn't actually verify that a given file is available through my server before sending a DMCA request. I've looked through the traffic logs, and the vast majority of the files listed in these takedown requests have never been requested in the history of my gateway. I haven't checked all of them, but I've checked a lot.

Maybe there's some site out there that has posted links to my gateway (which have never been used), and the CIU Online tool is picking up on those links without checking that they work. Or maybe they've identified that these files exist elsewhere on the IPFS network and they're sending takedown requests to all the IPFS gateways that they know about. For all I know, Covington and Burling could be hosting these files on their own IPFS node, just so they can send more DMCA requests to gateway operators.

I'd love to know if other gateway operators have gotten similar takedown requests.

## What is the point of all this?

Honestly, I don't know. Sometimes I think that they just send me these notifications to hassle me and waste my time.

As I mentioned previously, I've looked through the traffic logs, and nobody is requesting these files from my gateway. The nginx block rules almost never get triggered, so they're not even doing anything.

Also, I've tried to search for file sharing sites that might be linking to my gateway, but I haven't found anything.

Sending DMCA requests to an IPFS gateway is pointless. If people wanted to download these books, they would just download the local [IPFS tool](https://ipfs.tech/#install) and get them that way, without the use of a gateway. Or they would go to [Library Genesis](https://libgen.is/), since they probably exist there.
