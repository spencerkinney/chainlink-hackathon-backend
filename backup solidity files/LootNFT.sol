// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.7.0/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.7.0/contracts/access/Ownable.sol";

contract LootNFT is ERC721URIStorage, Ownable {
    string constant TOKEN_URI = "https://ipfs.io/ipfs/QmfUmppKG3Y8YZwgJHwBmgLVrpBGWsdNBspHCtpveQnTbU";
    uint256 internal tokenId;

    // Constructor
    constructor() ERC721("LootNFT", "MNFT") {}

    function mint(address to) public onlyOwner {
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, TOKEN_URI);
        unchecked {
            tokenId++;
        }
    }
}
