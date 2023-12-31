import React from 'react'
import styled from "styled-components";

function SidebarOption({Icon, title}) {
    return (
        <SidebarOptionContainer>
            {Icon && <Icon fontSize="small" style={{
                padding: 7
            }} />}
            {Icon ? (
                <h3>{title}</h3>
            ): (
                <SidebarOptionChannel>
                    <span>#</span> {title}
                </SidebarOptionChannel>
            )}
        </SidebarOptionContainer>
    )

}

export default SidebarOption;

const SidebarOptionContainer = styled.div`
    display: flex;
    font-size: 10px;
    align-item: center;
    padding-left: 2px;
    cursor: pointer;
    
    :hover {
        opacity: 0.9;
        background-color: #340e36
    }
`;
const SidebarOptionChannel = styled.div`

`;