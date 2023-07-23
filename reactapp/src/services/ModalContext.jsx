import Modal from "components/Modal";
import React, { createContext, useContext, useEffect, useState } from "react";
import ReactDOM from "react-dom";
import { useLocation } from "react-router-dom";
import { v4 as uuidv4 } from "uuid";

const Context = createContext(null);
const modalRoot = document.getElementById("modals");

// Gerencia todos os modais gerados
const ModalContextProvider = ({ children }) => {
  const [modals, setModals] = useState([]);
  const rootElemRef = React.useRef(document.createElement("div"));
  const navigate = useLocation();

  useEffect(() => {
    const elementRef = rootElemRef.current;
    if (modalRoot) {
      modalRoot.appendChild(elementRef);
    }
    return function removeElement() {
      elementRef.remove();
    };

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    setModals([]);
  }, [navigate]);

  function templateRemoveModal({ hook, id, params = {} }) {
    const _modals = modals.filter((modal) => modal.id !== id);
    setModals(_modals);
    hook(params);
  }

  function addModal({
    title,
    content,
    headerStyle,
    confirmButtonAction = () => {},
    returnButtonAction = () => {},
    ...rest
  }) {
    const id = uuidv4();
    setModals([
      ...modals,
      {
        id,
        tag: (
          <Modal
            key={id}
            headerTitle={title}
            headerStyle={headerStyle}
            confirmCallback={(params) =>
              templateRemoveModal({
                hook: confirmButtonAction,
                id,
                params,
              })
            }
            goBack={() =>
              templateRemoveModal({
                hook: returnButtonAction,
                id,
              })
            }
            {...rest}
          >
            {content}
          </Modal>
        ),
      },
    ]);
  }

  return (
    <Context.Provider value={{ addModal }}>
      {ReactDOM.createPortal(
        <>{modals.map((modal) => modal.tag)}</>,
        rootElemRef.current
      )}
      {children}
    </Context.Provider>
  );
};

export const useModalContext = () => useContext(Context);

export default ModalContextProvider;
