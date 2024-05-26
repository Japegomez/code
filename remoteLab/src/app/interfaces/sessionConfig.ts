export type GetSessionConfigResponse = {
  data: {
    attributes: {
      assigned_time: number
    }
    id: string
    relationships: {
      user: {
        data: {
          id: string
          type: string
        }
      }
    }
    type: string
  }
  included: Array<{
    attributes: {
      isActive: boolean
      name: string
    }
    id: string
    type: string
  }>
}
